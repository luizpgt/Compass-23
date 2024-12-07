from pydantic import BaseModel

class Booking(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    required_car_parking_space: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    repeated_guest: int
    no_of_special_requests: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    type_of_meal_plan: str
    room_type_reserved: str
    market_segment_type: str