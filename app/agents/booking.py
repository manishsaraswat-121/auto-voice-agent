class BookingAgent:
    def book(self, model: str, date: str, time: str):
        return {
            "model": model,
            "date": date,
            "time": time,
            "status": "confirmed"
        }
