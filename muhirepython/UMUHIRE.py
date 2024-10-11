class FitnessClassBooking:
    def __init__(self):
        self.available_classes = ["Yoga", "Pilates", "Spin", "Zumba", "HIIT"]
        self.scheduled_classes = [] 
        self.undo_stack = [] 

    def show_available_classes(self):
        print("Available Classes:")
        for fitness_class in self.available_classes:
            print(f"- {fitness_class}")

    def schedule_class(self, class_name):
        if class_name in self.available_classes:
            self.scheduled_classes.append(class_name)  
            self.undo_stack.append(class_name)  
            print(f"'{class_name}' scheduled.")
        else:
            print(f"'{class_name}' is not available.")

    def undo_booking(self):
        if self.undo_stack:
            last_booking = self.undo_stack.pop() 
            self.scheduled_classes.remove(last_booking)  
            print(f"Booking for '{last_booking}' undone.")
        else:
            print("No bookings to undo.")

    def show_scheduled_classes(self):
        print("Scheduled Classes:")
        if not self.scheduled_classes:
            print("No classes scheduled.")
        else:
            for fitness_class in self.scheduled_classes:
                print(f"- {fitness_class}")
booking_system = FitnessClassBooking()
booking_system.show_available_classes()
booking_system.schedule_class("Yoga")
booking_system.schedule_class("Zumba")
booking_system.show_scheduled_classes()
booking_system.undo_booking()
booking_system.show_scheduled_classes()
