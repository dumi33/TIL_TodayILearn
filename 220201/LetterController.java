// Body에 json 파일 형식으로 넣음
    @ResponseBody
    @PostMapping("")    // POST 방식의 요청을 매핑하기 위한 어노테이션
    public BaseResponse<PostLetterPlantRes> createLetter(@RequestBody PostLetterReq postLetterReq) {

        try{
            List<Integer> receiveUserIdx = letterService.createLetter(postLetterReq); // letter, letterSendList에 컬럼 추가
            // 화분 점수 증가
            PatchModifyScoreRes ModifyScore = plantService.modifyScore_plus(postLetterReq.getUserIdx(), Constant.PLANT_LEVELUP_LETTER,"letter");
            PostLetterPlantRes result_all = new PostLetterPlantRes(receiveUserIdx,ModifyScore ); // new 다음에 대문자여야한다.

            return new BaseResponse<>(result_all);
        } catch (BaseException exception){
            return new BaseResponse<>(exception.getStatus());
        }

    }
