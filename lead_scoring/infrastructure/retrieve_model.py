from google.cloud import storage
import os
import pickle5 as pickle



def retrieve_model(bucket_name, source_blob_name):
    """Import pickle model already trained form bucket.

    Arguments
    ---------
    bucket_name: str
        Bucket name.
    source_blob_name: str
        Path to the file trained model in bucket.

    Return
    ------
    model: scikit-learn Pipeline
        Fitted pipeline.
    """
    # Google Storage Client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    pickle_in = blob.download_as_bytes()
    # Model as pickle
    model = pickle.loads(pickle_in)
    return model


if __name__=="__main__":
    model = retrieve_model("chaos-4", "model_lead_scoring.pkl")