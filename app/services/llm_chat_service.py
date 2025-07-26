from typing import List, Dict, Any, Optional

from app.domain.chat import Chat, Message
from app.services.gateways.chat_llm_client import ChatLLMClient


class LLMChatService:
    """LLM を用いたチャット応答生成のアプリケーションサービス"""

    def __init__(self, llm_client: ChatLLMClient):
        self._llm_client = llm_client

    async def invoke(
        self,
        messages: List[Message],
        schema: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """ユーザー入力を受け取り、LLM から応答を生成して返す"""
        if not messages:
            return {"success": False, "error": "メッセージが空です"}

        try:
            # ドメインオブジェクトを作成
            chat = Chat(messages)
            # AIチャット
            generated = await self._llm_client.chat(chat.messages, schema=schema)

            if isinstance(generated, dict):
                return {"success": True, "generated_json": generated}
            else:
                return {"success": True, "generated_text": generated}

        except Exception as e:
            return {"success": False, "error": str(e)}
