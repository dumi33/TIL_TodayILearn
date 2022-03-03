## 편지 전송 로직 


편지를 보내는 과정에서 <br>
또래의 수신을 원하는 user, 원하지 않는 user를 구분한다.<br><br>

또래의 수신을 원하는 경우 birth의 년도로 구분하여 +-5살의 차이의 user에게만 편지를 전송한다.<br>


이렇게 생각하고 코드를 만들었는데 <br>
만약 해당 나이대의 사람이 **5사람 이하라면?**<br>
여기에서 계속 에러가 발생하였다.<br><br>

그래서 5명이 이하라면 선정한 5명 이하의 또래에게 보내고 나머지 사람들을 랜덤으로 골라 5명을 맞추어 편지를 보내는 로직을 만들었다.<br><br>

```java
 // 편지 작성(POST)

    public PostLetterPlantRes createLetter(PostLetterReq postLetterReq) throws BaseException {
        try {
            int letterIdx = letterDao.createLetter(postLetterReq); // 편지 생성 //letter 테이블에 생성 // 생성한 편지의 letterIdx반환
            PostLetterUserSimilarIdx idx_similar =letterDao.getIdx_Similar(letterIdx); // 생성한 유저의 idx와 SimilarAge여부를 반환
            if (idx_similar.getUserSimilarAge() == 1){// 편지 발송 유저가 또래 편지 수신을 원할경우
                List<Integer> receiveUserIdx_similar =letterDao.getLetterUserIdx_Similar(idx_similar);
                    // 휴먼상태가 아닌 또래의 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < receiveUserIdx_similar.size(); i++) { //(최대 5명) 5명의 userIdx를 뽑는다. // 1명씩 테이블에 추가하므로 5번 반복
                    letterDao.createLetterSendList(letterIdx,receiveUserIdx_similar,i);
                }
                if (receiveUserIdx_similar.size() < 5 ){ // 또래의 유저가 5명 미만이라면
                    Map<Integer, Integer> letterIdxMap = new HashMap<>();
                    for (int pastSend : receiveUserIdx_similar) {
                        letterIdxMap.put(pastSend, 1); // 이미 편지를 보낸 유저의 값을 1로 지정
                    }
                    //  (5 - 선택된 유저) 만큼 랜덤으로 보낼 유저 인덱스의 리스트 만들기
                    List<Integer> receiveUserIdx_Random =letterDao.getLetterUserIdx_Random(idx_similar);
                    // 또래 이외에 (5 - 선택된 유저) 만큼 랜덤으로 선택한 유저에게 편지 발송
                    int sendUserIdx = 0;
                    int similar_size = receiveUserIdx_similar.size();
                    for (int j = 0; j < (5-similar_size); j++,sendUserIdx++){ // j 번만큼 편지 전송
                        int userIdx = receiveUserIdx_Random.get(sendUserIdx);
                        if (letterIdxMap.containsKey(userIdx)==true) { // 만약 이미 편지를 보낸 유저라면
                            j -= 1; // 편지를 보낸 수 줄임
                            continue;
                        }
                        letterDao.createLetterSendList(letterIdx,receiveUserIdx_Random,sendUserIdx);
                        receiveUserIdx_similar.add(userIdx);
                    }

                }
                PatchModifyScoreRes ModifyScore = plantService.modifyScore_plus(postLetterReq.getUserIdx(), Constant.PLANT_LEVELUP_LETTER,"letter");
                String senderNickName = getNickName(postLetterReq.getUserIdx());
                PostLetterPlantRes result_similar = new PostLetterPlantRes(letterIdx,senderNickName,receiveUserIdx_similar,ModifyScore );
                return result_similar;
            }
            else {// 편지 발송 유저가 또래 편지 수신을 원하지않는 경우
                // (최대 5명) userIdx를 뽑는다.
                List<Integer> receiveUserIdx =letterDao.getLetterUserIdx(idx_similar); // 휴먼상태가 아닌 user 5명을 랜덤으로 골라 편지 발송 //letterSendList에 추가
                for (int i = 0; i < receiveUserIdx.size(); i++) { // 1명씩 테이블에 추가 // 5명보다 작을경우 더이상 보낼 유저가 없는것이므로 나온 유저의 수 만큼만 편지를 전송한다. 
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
 <br><br>
 
 map을 이용하고 로직을 생각해내는 과정에서 꽤나 시간이 걸렸지만 <br>
 잘 돌아간다는 것에 뿌듯하다. 
