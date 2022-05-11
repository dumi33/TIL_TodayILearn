    # 모델 적용
    def get(self, img, max_num=0):
        # 모델 bbox, kpss
        # face detection
        bboxes, kpss = self.det_model.detect(img,
                                             threshold=self.det_thresh,
                                             max_num=max_num,
                                             metric='default')
        # bbox가 0이면 0 리턴
        if bboxes.shape[0] == 0:
            return []
        ret = []
        # 각각의 box에 대한 결과 추출
        for i in range(bboxes.shape[0]):
            # bbox 추출
            bbox = bboxes[i, 0:4]
            det_score = bboxes[i, 4]
            kps = None
            if kpss is not None:
                kps = kpss[i]
            embedding = None
            normed_embedding = None
            embedding_norm = None

            # face recognition
            if 'recognition' in self.models:
                assert kps is not None
                rec_model = self.models['recognition']
                aimg = norm_crop(img, landmark=kps)
                print(kps)
                embedding = None
                embedding_norm = None
                normed_embedding = None
                # 임베딩 값 추출
                embedding = rec_model.get_feat(aimg).flatten()
                embedding_norm = norm(embedding)
                normed_embedding = embedding / embedding_norm

            # face에 결과를 담음
            face = Face(bbox=bbox,
                        kps=kps,
                        det_score=det_score,
                        embedding=embedding,
                        normed_embedding=normed_embedding,
                        embedding_norm=embedding_norm)
            ret.append(face)
        return ret
