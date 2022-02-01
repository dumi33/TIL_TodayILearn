//해당 letterIdx를 갖는 편지의 isChecked를 1로 update // isChecked가 0이면 열람 X, 1이면 열람 O
    public int modifyIsChecked(int letterIdx, int userIdx) {
        String getReplyQuery = "update LetterSendList set isChecked=1 where letterIdx = ? and receiverIdx = ?"; // 해당 replyIdx를 만족하는 답장의 열람 여부를 변경하는 쿼리문
        Object[] modifyReplyStatusParams = new Object[]{letterIdx, userIdx}; // 주입될 값 (replyIdx)

        return this.jdbcTemplate.update(getReplyQuery, modifyReplyStatusParams); // 대응시켜 매핑시켜 쿼리 요청(선공했으면 1, 실패했으면 0)
    }
