from collections import defaultdict


class MemoryService:

    def __init__(self):
        self.sessions = defaultdict(list)

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
    ):
        self.sessions[session_id].append(
            {
                "role": role,
                "content": content,
            }
        )

    def get_history(self, session_id: str):
        return self.sessions.get(session_id, [])

    def get_context(
        self,
        session_id: str,
        max_messages: int = 8,
    ):
        """
        Returns the latest conversation formatted
        for insertion into the LLM prompt.
        """

        history = self.get_history(session_id)[-max_messages:]

        if not history:
            return "No previous conversation."

        conversation = []

        for message in history:
            conversation.append(
                f"{message['role']}: {message['content']}"
            )

        return "\n".join(conversation)

    def clear_history(self, session_id: str):
        self.sessions.pop(session_id, None)


memory_service = MemoryService()