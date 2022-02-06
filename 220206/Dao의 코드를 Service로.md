Dao에는 쿼리 관련 코드들만 있는것이 좋다고 하여 Dao에 작성하였던 로직들을 service로 옮기도록 코드를 수정하였다. 

## - 수정 전 로직이 포함된 Dao의 POST 메서드
```java
// 편지 발송 // letterSendList에 isSad상태가 아닌 userIdx 5개를 골라 SendList에 컬럼 추가하는 함수
    public List<Integer> createLetterSendList(int letterIdx) { // 생성된 letter의 Idx를 인수로 받는다.
        //해당 편지를 발송한 userIdx
        String getUserIdxQuery = "SELECT L.userIdx FROM Letter L WHERE L.letterIdx=?";
        int getUserIdxParam = letterIdx;
        int userIdx = this.jdbcTemplate.queryForObject(getUserIdxQuery, int.class, getUserIdxParam);
        // 편지 발송 유저의 또래 편지 수신 여부
        String getSimilarAgeQuery = "SELECT U.recSimilarAge FROM User U WHERE userIdx=?";
        int userSimilarAge = this.jdbcTemplate.queryForObject(getSimilarAgeQuery, int.class, userIdx);

        if (userSimilarAge==1){ // 편지 발송 유저가 또래 편지 수신을 원할경우

            String getBirthQuery = "SELECT U.birth FROM User U WHERE userIdx=?"; // 해당 유저의 생년을 구한다.
            int userBirth = this.jdbcTemplate.queryForObject(getBirthQuery, int.class, userIdx);

            String getUserIdx = "select U.userIdx from User U where U.status='active' and U.recOthers = 1 and ( (?-5) <= U.birth and U.birth <=(?+5))  order by rand() limit 5";
            // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저이고, 나이대가 +-5년의 유저 중
            // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
            List<Integer> userIdx_Similar = this.jdbcTemplate.queryForList(getUserIdx, int.class,userBirth,userBirth); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

            for (int i= 0; i<5 ; i++){ // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                String createLetterSendListQuery = "insert into LetterSendList (letterIdx,receiverIdx) VALUES (?,?)"; // 실행될 동적 쿼리문
                Object[] createLetterSendListParams = new Object[]{letterIdx,userIdx_Similar.get(i)}; // 동적 쿼리의 ?부분에 주입될 값
                this.jdbcTemplate.update(createLetterSendListQuery, createLetterSendListParams);
            }
            return userIdx_Similar;
        }

        else { //편지 발송 유저가 또래 편지 수신을 원하지 않을경우
            String getUserIdx = "select U.userIdx from User U where U.status='active' and recOthers = 1 order by rand() limit 5";
            // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저 중
            // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
            List<Integer> userIdx_unSimilar = this.jdbcTemplate.queryForList(getUserIdx, int.class); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

            for (int i= 0; i<5 ; i++){ // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                String createLetterSendListQuery = "insert into LetterSendList (letterIdx,receiverIdx) VALUES (?,?)"; // 실행될 동적 쿼리문
                Object[] createLetterSendListParams = new Object[]{letterIdx,userIdx_unSimilar.get(i)}; // 동적 쿼리의 ?부분에 주입될 값
                this.jdbcTemplate.update(createLetterSendListQuery, createLetterSendListParams);
            }
            return userIdx_unSimilar;
        }

    }
```
<br><br>

## - 수정 후 로직을 service로 옮기고 쿼리문만 있은 Dao
```java
public PostLetterUserSimilarIdx getIdx_Similar(int letterIdx) { //편지를 전송하는 사람의 userIdx와 similarAge의 여부를 반환
        String getUserIdxQuery = "SELECT L.userIdx FROM Letter L WHERE L.letterIdx=?";
        int userIdx = this.jdbcTemplate.queryForObject(getUserIdxQuery, int.class, letterIdx);
        // 편지 발송 유저의 또래 편지 수신 여부
        String getSimilarAgeQuery = "SELECT U.recSimilarAge FROM User U WHERE userIdx=?";
        int userSimilarAge = this.jdbcTemplate.queryForObject(getSimilarAgeQuery, int.class, userIdx);
        PostLetterUserSimilarIdx userIdx_SimilarAge = new PostLetterUserSimilarIdx(userIdx, userSimilarAge);
        return userIdx_SimilarAge;
    }

    public List<Integer> getLetterUserIdx_Similar(PostLetterUserSimilarIdx postLetterUserSimilarIdx) {
        String getBirthQuery = "SELECT U.birth FROM User U WHERE userIdx=?"; // 해당 유저의 생년을 구한다.
        int getUserIdxParam = postLetterUserSimilarIdx.getUserIdx();
        int userBirth = this.jdbcTemplate.queryForObject(getBirthQuery, int.class, getUserIdxParam);

        String getUserIdx = "select U.userIdx from User U where U.status='active' and U.recOthers = 1 and ( (?-5) <= U.birth and U.birth <=(?+5))  order by rand() limit 5";
        // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저이고, 나이대가 +-5년의 유저 중
        // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
        List<Integer> userIdx_Similar = this.jdbcTemplate.queryForList(getUserIdx, int.class, userBirth, userBirth); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

        return userIdx_Similar;
    }

    public void createLetterSendList(int letterIdx, List<Integer> userIdx_list,int i){
        String createLetterSendListQuery = "insert into LetterSendList (letterIdx,receiverIdx) VALUES (?,?)"; // 실행될 동적 쿼리문
        Object[] createLetterSendListParams = new Object[]{letterIdx, userIdx_list.get(i)}; // 동적 쿼리의 ?부분에 주입될 값
        this.jdbcTemplate.update(createLetterSendListQuery, createLetterSendListParams);
    }

    public List<Integer> getLetterUserIdx (PostLetterUserSimilarIdx postLetterUserSimilarIdx) {
        String getUserIdx = "select U.userIdx from User U where U.status='active' and recOthers = 1 order by rand() limit 5";
        // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저 중
        // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
        List<Integer> userIdx_unSimilar = this.jdbcTemplate.queryForList(getUserIdx, int.class); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

        return userIdx_unSimilar;
    }

    //편지 삭제 // 해당 letterIdx의 편지 status를 deleted로 변경
    public int modifyLetterStatus(PatchLetterReq patchLetterReq) {
        String modifyLetterStatusQuery = "update Letter set status = ? where letterIdx = ? "; // 해당 userIdx를 만족하는 User를 해당 nickname으로 변경한다.
        Object[] modifyLetterStatusParams = new Object[]{"deleted", patchLetterReq.getLetterIdx()}; // 주입될 값들(status, letterIdx) 순

        return this.jdbcTemplate.update(modifyLetterStatusQuery, modifyLetterStatusParams); // 대응시켜 매핑시켜 쿼리 요청(생성했으면 1, 실패했으면 0)
    }
```
<br><br>
## - 로직을 포함한 Service.java
```java
// 편지 작성(POST)

    public List<Integer> createLetter(PostLetterReq postLetterReq) throws BaseException {

        try {
            int letterIdx = letterDao.createLetter(postLetterReq); // 편지 생성 //letter 테이블에 생성 // 생성한 편지의 letterIdx반환
            PostLetterUserSimilarIdx idx_similar =letterDao.getIdx_Similar(letterIdx); // 생성한 유저의 idx와 SimilarAge여부를 반환

            if (idx_similar.getUserSimilarAge() == 1){// 편지 발송 유저가 또래 편지 수신을 원할경우
                List<Integer> receiveUserIdx_similar =letterDao.getLetterUserIdx_Similar(idx_similar); // 휴먼상태가 아닌 또래의 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx_similar,i);
                }
                return receiveUserIdx_similar;
            }

            else {// 편지 발송 유저가 또래 편지 수신을 원하지않는 경우
                List<Integer> receiveUserIdx =letterDao.getLetterUserIdx(idx_similar); // 휴먼상태가 아닌 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx,i);
                }
                return receiveUserIdx;
            }

        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지를 보냅니다.
            exception.printStackTrace(); // 에러 발생 원인 출력
            throw new BaseException(DATABASE_ERROR);
        }
    }
    ```
    
    

