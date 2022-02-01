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
