def Create_Embedding(addr) :
    from library import arcface_onnx
    from library import model_zoo
    from library import face_analysis
    from library import model_func
    import onnxruntime


    app = model_func.model_prepare('models')
    
    evaluation_embs, evaluation_labels = model_func.embs_result(addr, app)
    return evaluation_embs, evaluation_labels
