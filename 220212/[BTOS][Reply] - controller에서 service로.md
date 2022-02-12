## <변경 전 >

- Controller 


```java
 /**
     * 답장 작성 API
     * [POST] /replies
     */

    // Body
    @ResponseBody
    @PostMapping("")    // POST 방식의 요청을 매핑하기 위한 어노테이션
    public BaseResponse<PostReplyFinalRes> createReply(@RequestBody PostReplyReq postReplyReq) {
        //  @RequestBody란, 클라이언트가 전송하는 HTTP Request Body(우리는 JSON으로 통신하니, 이 경우 body는 JSON)를 자바 객체로 매핑시켜주는 어노테이션
        try{
            int replyIdx = replyService.createReply(postReplyReq);
            PostReplyRes postReplyRes = replyService.getReplyreceiverNickname(postReplyReq); // 받는 유저의 userIdx, 답장을 보내는 사람의 닉네임 반환
            PostReplyFinalRes postReplyFinalRes = new PostReplyFinalRes(replyIdx,postReplyRes.getReceiverIdx(),postReplyRes.getSenderNickName());
            return new BaseResponse<>(postReplyFinalRes);
        } catch (BaseException exception){
            return new BaseResponse<>((exception.getStatus()));
        }
    }
```

<br>

- Service

```java
    // 답장 작성(POST)

    public int createReply(PostReplyReq postReplyReq) throws BaseException {

        try {
            int replyIdx = replyDao.createReply(postReplyReq);
            return replyIdx;

        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지 : 8004

            throw new BaseException(REPLY_DATABASE_ERROR);
        }
    }

    // POST - nickName을 찾고 PostReplyFinalRes 객체를 만들어 반환 
    public PostReplyRes getReplyreceiverNickname(PostReplyReq postReplyReq) throws BaseException {

        try {
            String senderNickName = replyDao.getNickname(postReplyReq.getReplierIdx());
            PostReplyRes postReplyRes = new PostReplyRes(postReplyReq.getReceiverIdx(),senderNickName );
            return postReplyRes;

        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지 : 8004

            throw new BaseException(REPLY_DATABASE_ERROR);
        }
    }
```

<br><br>

## 변경 후 


- Controller 

```java
/**
     * 답장 작성 API
     * [POST] /replies
     */

    // Body
    @ResponseBody
    @PostMapping("")    // POST 방식의 요청을 매핑하기 위한 어노테이션
    public BaseResponse<PostReplyFinalRes> createReply(@RequestBody PostReplyReq postReplyReq) {
        //  @RequestBody란, 클라이언트가 전송하는 HTTP Request Body(우리는 JSON으로 통신하니, 이 경우 body는 JSON)를 자바 객체로 매핑시켜주는 어노테이션
        try{
            PostReplyFinalRes postReplyFinalRes = replyService.createReply(postReplyReq);
            return new BaseResponse<>(postReplyFinalRes);
        } catch (BaseException exception){
            return new BaseResponse<>((exception.getStatus()));
        }
    }
```

<br>

- service

```java
// 답장 작성(POST)

    public PostReplyFinalRes createReply(PostReplyReq postReplyReq) throws BaseException {

        try {
            int replyIdx = replyDao.createReply(postReplyReq);
            PostReplyFinalRes postReplyFinalRes = getReplyreceiverNickname(replyIdx,postReplyReq); // 받는 유저의 userIdx, 답장을 보내는 사람의 닉네임 반환

            return postReplyFinalRes;

        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지 : 8004

            throw new BaseException(REPLY_DATABASE_ERROR);
        }
    }

    // POST - nickName을 찾고 PostReplyFinalRes 객체를 만들어 반환

    public PostReplyFinalRes getReplyreceiverNickname(int replyIdx, PostReplyReq postReplyReq) throws BaseException {

        try {
            String senderNickName = replyDao.getNickname(postReplyReq.getReplierIdx());
            PostReplyFinalRes postReplyFinalRes = new PostReplyFinalRes(replyIdx,postReplyReq.getReceiverIdx(),senderNickName );
            return postReplyFinalRes;
        } catch (Exception exception) { // DB에 이상이 있는 경우 에러 메시지 : 8004

            throw new BaseException(REPLY_DATABASE_ERROR);
        }
    }
```

- 필요없는 객체인 PostReplyRes를 삭제하였다. 




