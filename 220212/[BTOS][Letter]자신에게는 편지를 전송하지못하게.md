

비슷한 연령대의  유저에게 편지를 보낼 때 유저들 중 무작위로 뽑다보니 자기 자신에게 편지를 보내는 일이 발생하였다. <br>
랜덤으로 보낼 사람을 뽑는 쿼리문을 **자기 자신의 userIdx는 제외하도록** 변경하였다. 



## <변경 전>

```java
public List<Integer> getLetterUserIdx_Similar(PostLetterUserSimilarIdx postLetterUserSimilarIdx) { // 편지를 수신할 유저의 userIdx들을 list형태로 반환 // +-5살의 유저만 선택
        String getBirthQuery = "SELECT U.birth FROM User U WHERE userIdx=?"; // 해당 유저의 생년을 구한다.
        int getUserIdxParam = postLetterUserSimilarIdx.getUserIdx();
        int userBirth = this.jdbcTemplate.queryForObject(getBirthQuery, int.class, getUserIdxParam);

        String getUserIdx = "select U.userIdx from User U where U.status='active'and U.recOthers = 1 and ( (?-5) <= U.birth and U.birth <=(?+5))  order by rand() limit 5";
        // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저이고, 나이대가 +-5년의 유저 중 
        // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
        List<Integer> userIdx_Similar = this.jdbcTemplate.queryForList(getUserIdx, int.class, userBirth, userBirth); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

        return userIdx_Similar;
    }
```

<br>

## <변경 후>

```java
public List<Integer> getLetterUserIdx_Similar(PostLetterUserSimilarIdx postLetterUserSimilarIdx) { // 편지를 수신할 유저의 userIdx들을 list형태로 반환 // +-5살의 유저만 선택
        String getBirthQuery = "SELECT U.birth FROM User U WHERE userIdx=?"; // 해당 유저의 생년을 구한다.
        int getUserIdxParam = postLetterUserSimilarIdx.getUserIdx();
        int userBirth = this.jdbcTemplate.queryForObject(getBirthQuery, int.class, getUserIdxParam);

        String getUserIdx = "select U.userIdx from User U where U.status='active' and U.userIdx != ? and U.recOthers = 1 and ( (?-5) <= U.birth and U.birth <=(?+5))  order by rand() limit 5";
        // 휴먼상태가 아니고, 타인의 편지를 수신하는 유저이고, 나이대가 +-5년의 유저 중 (편지를 보내는 유저 제외)
        // 랜덤으로 5명의 userIdx를 뽑는 쿼리문
        List<Integer> userIdx_Similar = this.jdbcTemplate.queryForList(getUserIdx, int.class,getUserIdxParam, userBirth, userBirth); // 변수 userIdx에 랜덤으로 뽑은 userIdx를 넣는다.

        return userIdx_Similar;
    }
```
