import os
from fastapi import APIRouter
import json
import boto3

# boto3를 사용하여 SQS 클라이언트를 생성합니다.
sqs = boto3.client('sqs')
# 환경 변수에서 SQS 응답 큐 URL을 가져옵니다. 필요에 따라 수정하세요.
RESPONSE_QUEUE_URL = os.environ.get("RESPONSE_QUEUE_URL")

router = APIRouter()

@router.get("/result/{request_id}")
async def get_result(request_id: str):
    response = sqs.receive_message(
        QueueUrl=RESPONSE_QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )

    if "Messages" in response:
        for message in response["Messages"]:
            body = json.loads(message["Body"])

            if body["request_id"] == request_id:
                result = body["result"]

                # 처리된 메시지는 삭제
                sqs.delete_message(
                    QueueUrl=RESPONSE_QUEUE_URL,
                    ReceiptHandle=message["ReceiptHandle"]
                )

                return {"status": "completed", "result": result}

    return {"status": "processing", "message": "Request is still being processed"}