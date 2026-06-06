// ========== SUBSYSTEM CLASSES (Complex Systems) ==========

// Hotel subsystem
class HotelSystem {
    public void bookRoom() {
        System.out.println("  → Hotel: Room booked successfully");
    }
    
    public String getRoomStatus() {
        return "Available";
    }
    
    public void checkIn(String guestName) {
        System.out.println("  → Hotel: Guest " + guestName + " checked in");
    }
}

// Restaurant subsystem
class RestaurantSystem {
    public void orderFood(String item) {
        System.out.println("  → Restaurant: Ordering " + item);
    }
    
    public void payBill() {
        System.out.println("  → Restaurant: Bill paid - ₹1200");
    }
    
    public String getMenu() {
        return "Veg: Biryani, Pasta | Non-Veg: Chicken Curry, Steak";
    }
}

// Transport subsystem
class TransportSystem {
    public void bookTaxi() {
        System.out.println("  → Transport: Lyft Taxi booked - ID: TX4589");
    }
    
    public void scheduleAirportDrop() {
        System.out.println("  → Transport: Airport drop scheduled for 6:00 PM");
    }
}

// ========== FACADE CLASS (Simplified Interface) ==========

class HotelFacade {
    private HotelSystem hotel;
    private RestaurantSystem restaurant;
    private TransportSystem transport;
    
    public HotelFacade() {
        this.hotel = new HotelSystem();
        this.restaurant = new RestaurantSystem();
        this.transport = new TransportSystem();
    }
    
    // Simple method orchestrating multiple subsystem calls
    public void arrangeFullStay(String guestName, String foodItem) {
        System.out.println("=== Arranging Full Stay for " + guestName + " ===");
        hotel.bookRoom();
        hotel.checkIn(guestName);
        restaurant.orderFood(foodItem);
        transport.bookTaxi();
        restaurant.payBill();
        transport.scheduleAirportDrop();
        System.out.println("=== Stay Arranged Successfully ===\n");
    }
    
    public String checkAvailability() {
        return "Room Status: " + hotel.getRoomStatus();
    }
    
    public String getMenu() {
        return restaurant.getMenu();
    }
}

// ========== CLIENT CODE ==========

public class FacadeDemo {
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════╗");
        System.out.println("  Facade Design Pattern - Java Demo");
        System.out.println("╚════════════════════════════════════════╝\n");
        
        HotelFacade facade = new HotelFacade();
        
        System.out.println("1️⃣ USING FACADE (Simple Interface):");
        facade.arrangeFullStay("Rahul Sharma", "Biryani");
        
        System.out.println("2️⃣ Checking Availability:");
        System.out.println("   " + facade.checkAvailability());
        System.out.println("   Menu: " + facade.getMenu());
        
        System.out.println("\n3️⃣ WITHOUT FACADE (Complex - What Client Avoids):");
        System.out.println("   Would need 6 separate calls:");
        System.out.println("   • hotelSystem.bookRoom()");
        System.out.println("   • hotelSystem.checkIn(name)");
        System.out.println("   • restaurantSystem.orderFood(item)");
        System.out.println("   • transportSystem.bookTaxi()");
        System.out.println("   • restaurantSystem.payBill()");
        System.out.println("   • transportSystem.scheduleAirportDrop()");
        
        System.out.println("\n4️⃣ FACADE BENEFITS:");
        System.out.println("   ✓ Simplifies complex subsystem interactions [web:1]");
        System.out.println("   ✓ Provides single entry point [web:3]");
        System.out.println("   ✓ Reduces client-subsystem dependencies [web:3]");
        System.out.println("   ✓ Improves maintainability [web:1]");
        System.out.println("   ✓ Decouples client from subsystem changes [web:1]");
        
        System.out.println("\n5️⃣ REAL-WORLD ANALOGY:");
        System.out.println("   🏨 Hotel Reception = Facade");
        System.out.println("   You tell ONE person what you need,");
        System.out.println("   they coordinate housekeeping, kitchen, transport!");
    }
}
