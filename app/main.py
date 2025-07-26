"""全てのルーティングを管理"""
import asyncio
from typing import List
from app.services.llm_chat_service import LLMChatService
from app.infrastructure.bedrock_chat_llm_client import BedrockChatLLMClient
from app.domain.chat import Message, Chat


async def main():
    """
    チャット形式での会話エンドポイント
    
    会話履歴を考慮してBedrockが返答を生成します。
    roleは'user'（ユーザー）または'assistant'（AI）を指定してください。
    """
    llm_client = BedrockChatLLMClient()
    # 依存性注入：インフラ層をアプリケーションサービスに注入
    chat_service = LLMChatService(llm_client)
    

    messages: List[Message] = [
        Message(role="user", content="東京の良いところは？")
    ]
    
    result = await chat_service.invoke(messages, schema=None)
    print("チャット結果:", result)
    return result


if __name__ == "__main__":
    print("チャットサービスを開始します...")
    result = asyncio.run(main())
    print("完了しました。")
