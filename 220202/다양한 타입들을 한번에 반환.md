## 다양한 타입들을 한번에 반환하는 법


### report 도메인에서 원래 반환값 + 신고된 유저의 Idx를 함께 반환하도록 코드 변경

#### ReportController.java
```java
 @ResponseBody
    @PostMapping("")    // POST 어노테이션
    public BaseResponse<String> createReport(@RequestBody PostReportReq postReportReq) {
    public BaseResponse<PostReportUserIdxPlantRes> createReport(@RequestBody PostReportReq postReportReq) {
        try{
            String ReportReason = postReportReq.getReason(); // 신고 사유 // spam : 스팸 / sex : 성적 / hate : 혐오 / dislike : 마음에 안듦 / etc : 기타
            reportService.createReport(postReportReq);
             if ((ReportReason.equals("sex")) || (ReportReason.equals("hate"))) {
             // 화분 점수 감소 //-100
                plantService.modifyScore_minus(reportService.getUserIdx(postReportReq), Constant.PLANT_LEVELDOWN_REPORT_SEX_HATE, "report_sex_hate");
                 PatchModifyScoreRes ModifyScore_sex_hate = plantService.modifyScore_minus(reportService.getUserIdx(postReportReq), Constant.PLANT_LEVELDOWN_REPORT_SEX_HATE, "report_sex_hate");
                 PostReportUserIdxPlantRes result_sex_hate = new PostReportUserIdxPlantRes(reportService.getUserIdx(postReportReq), ModifyScore_sex_hate );
                 return new BaseResponse<>(result_sex_hate);
             } else if ((ReportReason.equals("spam")) || (ReportReason.equals("dislike"))) {
             // 화분 점수 감소 // -30
                plantService.modifyScore_minus(reportService.getUserIdx(postReportReq), Constant.PLANT_LEVELDOWN_REPORT_SPAM_DISLIKE, "report_spam_dislike");
                 PatchModifyScoreRes ModifyScore_spam_dislike = plantService.modifyScore_minus(reportService.getUserIdx(postReportReq), Constant.PLANT_LEVELDOWN_REPORT_SPAM_DISLIKE, "report_spam_dislike");
                 PostReportUserIdxPlantRes result_spam_dislike = new PostReportUserIdxPlantRes(reportService.getUserIdx(postReportReq), ModifyScore_spam_dislike );
                 return new BaseResponse<>(result_spam_dislike);
             }
             else if ((ReportReason.equals("etc"))) {
             String result = "신고-(기타)가 완료되었습니다.";
             return new BaseResponse<>(result);
                 PatchModifyScoreRes ModifyScore_null = new PatchModifyScoreRes(false,"report_etc");
                 PostReportUserIdxPlantRes result_etc = new PostReportUserIdxPlantRes(reportService.getUserIdx(postReportReq), ModifyScore_null );
                 return new BaseResponse<>(result_etc);
             }
             else {
                 throw new BaseException(POST_REPORT_REASON);
             }
            String result = "신고가 완료되었습니다.";
            return new BaseResponse<>(result);
        } catch (BaseException exception){

            return new BaseResponse<>((exception.getStatus()));
```

한번에 두개의 타입을 반환하도록 PostReportUserIdxPlantRes를 생성하였다.
PostReportUserIdxPlantRes는 유저 인덱스와 원래 반환하던 PatchModifyScoreRes가 함께 들어있다.

#### PostReportUserIdxPlantRes.java

```java
@Getter
@Setter
@AllArgsConstructor
public class PostReportUserIdxPlantRes {
    private int reportedUserIdx; // 신고당한 유저의 Idx
    private PatchModifyScoreRes patchModifyScoreRes; // 화분점수 변경 반환
}
```

java에서는 반환형이 있는 이상 반환이 꼭 필요하다.
그래서 if, else if 로만 이루어질 경우 빨간줄이 뜬다.
그래서 else 로 이상한값을 만들어 반환하곤 했었는데
팀원의 코드를 참조하여 위와 같은 코드로 만들었다.

```java
else {
                 throw new BaseException(POST_REPORT_REASON);
             }
```





