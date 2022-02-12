## <변경 전>

요청 : controller 말고 Service에 변수들이 있게 해주세요!

- Controller 
```java
/**
     * 편지 작성 API
     * [POST] /letters
     */

    // Body에 json 파일 형식으로 넣음
    @ResponseBody
    @PostMapping("")    // POST 방식의 요청을 매핑하기 위한 어노테이션
    public BaseResponse<PostLetterPlantRes> createLetter(@RequestBody PostLetterReq postLetterReq) {

        try{
            PostLetterRes postLetterRes = letterService.createLetter(postLetterReq);
            // 화분 점수 증가
            PatchModifyScoreRes ModifyScore = plantService.modifyScore_plus(postLetterReq.getUserIdx(), Constant.PLANT_LEVELUP_LETTER,"letter");
            String senderNickName = letterService.getNickName(postLetterReq.getUserIdx());
            PostLetterPlantRes result_all = new PostLetterPlantRes(postLetterRes.getLetterIdx(),senderNickName,postLetterRes.getReceiverIdxList(),ModifyScore ); // new 다음에 대문자여야한다.

            return new BaseResponse<>(result_all);
        } catch (BaseException exception){
            return new BaseResponse<>(exception.getStatus());
        }

    }
``` 
<br>

- Service

```java
// 편지 작성(POST)

    public PostLetterRes createLetter(PostLetterReq postLetterReq) throws BaseException {
        try {
            int letterIdx = letterDao.createLetter(postLetterReq); // 편지 생성 //letter 테이블에 생성 // 생성한 편지의 letterIdx반환
            PostLetterUserSimilarIdx idx_similar =letterDao.getIdx_Similar(letterIdx); // 생성한 유저의 idx와 SimilarAge여부를 반환
            if (idx_similar.getUserSimilarAge() == 1){// 편지 발송 유저가 또래 편지 수신을 원할경우
                List<Integer> receiveUserIdx_similar =letterDao.getLetterUserIdx_Similar(idx_similar);
                    // 휴먼상태가 아닌 또래의 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx_similar,i);
                }
                PostLetterRes postLetterRes_similar = new PostLetterRes(letterIdx, receiveUserIdx_similar );
                return postLetterRes_similar;
            }
            else {// 편지 발송 유저가 또래 편지 수신을 원하지않는 경우
                    List<Integer> receiveUserIdx =letterDao.getLetterUserIdx(idx_similar); // 휴먼상태가 아닌 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                    for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                        letterDao.createLetterSendList(letterIdx,receiveUserIdx,i);
                    }
                PostLetterRes postLetterRes = new PostLetterRes(letterIdx, receiveUserIdx );
                    return postLetterRes;
            }
        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지를 보냅니다.
            exception.printStackTrace(); // 에러 발생 원인 출력
            throw new BaseException(DATABASE_ERROR);
        }
    }
```
<br><br>

## <변경 후>

- controller
```java
 /**
     * 편지 작성 API
     * [POST] /letters
     */

    // Body에 json 파일 형식으로 넣음
    @ResponseBody
    @PostMapping("")    // POST 방식의 요청을 매핑하기 위한 어노테이션
    public BaseResponse<PostLetterPlantRes> createLetter(@RequestBody PostLetterReq postLetterReq) {

        try{
            PostLetterPlantRes postLetterPlantRes = letterService.createLetter(postLetterReq);
            // 화분 점수 증가
            return new BaseResponse<>(postLetterPlantRes);
        } catch (BaseException exception){
            return new BaseResponse<>(exception.getStatus());
        }

    }
 ```
 <br>
 
 - Service

```java
// 편지 작성(POST)

    public PostLetterPlantRes createLetter(PostLetterReq postLetterReq) throws BaseException {
        try {
            int letterIdx = letterDao.createLetter(postLetterReq); // 편지 생성 //letter 테이블에 생성 // 생성한 편지의 letterIdx반환
            PostLetterUserSimilarIdx idx_similar =letterDao.getIdx_Similar(letterIdx); // 생성한 유저의 idx와 SimilarAge여부를 반환
            if (idx_similar.getUserSimilarAge() == 1){// 편지 발송 유저가 또래 편지 수신을 원할경우
                List<Integer> receiveUserIdx_similar =letterDao.getLetterUserIdx_Similar(idx_similar);
                    // 휴먼상태가 아닌 또래의 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx_similar,i);
                }
                PatchModifyScoreRes ModifyScore = plantService.modifyScore_plus(postLetterReq.getUserIdx(), Constant.PLANT_LEVELUP_LETTER,"letter");
                String senderNickName = getNickName(postLetterReq.getUserIdx());
                PostLetterPlantRes result_similar = new PostLetterPlantRes(letterIdx,senderNickName,receiveUserIdx_similar,ModifyScore );
                return result_similar;
            }
            else {// 편지 발송 유저가 또래 편지 수신을 원하지않는 경우
                List<Integer> receiveUserIdx =letterDao.getLetterUserIdx(idx_similar); // 휴먼상태가 아닌 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < 5; i++) { // 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx,i);
                }
                PatchModifyScoreRes ModifyScore = plantService.modifyScore_plus(postLetterReq.getUserIdx(), Constant.PLANT_LEVELUP_LETTER,"letter");
                String senderNickName = getNickName(postLetterReq.getUserIdx());
                PostLetterPlantRes result = new PostLetterPlantRes(letterIdx,senderNickName,receiveUserIdx,ModifyScore );
                return result;
            }
        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지를 보냅니다.
            exception.printStackTrace(); // 에러 발생 원인 출력
            throw new BaseException(DATABASE_ERROR);
        }
    }
```

Controller에는 최대한 간결하게!!
 
