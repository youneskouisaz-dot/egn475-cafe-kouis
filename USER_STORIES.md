Café Calle Ocho — User Stories and Acceptance Criteria
Course: EGN475 — PrototypingPersonas: Marta Alvarez (Customer) and Luis Rodriguez (Kitchen Staff)

US-01: View Café Menu

Must-have

Customer
As a café customer, I want to view the menu with item names, prices, and availability, so that I can decide what to order.
AC1 — Normal: Given the café has available menu items, when I open the menu page, then I can see each item's name, price, and availability.

AC2 — Edge case: Given there are no menu items available, when I open the menu page, then I see a message saying that no items are currently available.


US-02: Add Items to an Order

Must-have

Customer
As a café customer, I want to add menu items to my order, so that I can select the food and drinks I want.
AC1 — Normal: Given a menu item is available, when I click Add to Order, then the item appears in my order.

AC2 — Edge case: Given a menu item is sold out, when I attempt to add it, then the item is not added and I see an unavailable message.


US-03: View Order Summary

Must-have

Customer
As a café customer, I want to see my selected items and total price, so that I can review my order before submitting it.
AC1 — Normal: Given I have added items to my order, when I open the order summary, then I see each selected item and the correct total price.

AC2 — Edge case: Given my order is empty, when I open the order summary, then I see an empty-order message and a total of $0.00.


US-04: Submit an Order

Must-have

Customer
As a café customer, I want to place my order and receive an order number, so that I know my order was successfully received.
AC1 — Normal: Given my order contains at least one available item, when I click Place Order, then my order is submitted and I receive a confirmation with an order number.

AC2 — Edge case: Given my order is empty, when I click Place Order, then the order is not submitted and I see a message asking me to add an item.


US-05: Track Order Status

Must-have

Customer
As a café customer, I want to check the preparation status of my order, so that I know when it is ready for pickup.
AC1 — Normal: Given I have a valid order number, when I check my order status, then I see its current status, such as Received, Preparing, or Ready.

AC2 — Edge case: Given I enter an invalid order number, when I check the status, then I see a message that the order was not found.


US-06: View Incoming Orders

Must-have

Staff
As a kitchen staff member, I want to view incoming customer orders, so that I know which meals and drinks need to be prepared.
AC1 — Normal: Given customers have submitted orders, when I open the kitchen order board, then I see the incoming orders with their order numbers and items.

AC2 — Edge case: Given there are no incoming orders, when I open the kitchen order board, then I see a message saying there are no pending orders.


US-07: Update Order Status

Should-have

Staff
As a kitchen staff member, I want to change an order's status, so that customers can follow its preparation progress.
AC1 — Normal: Given an order has the status Received, when I click Start Preparing, then its status changes to Preparing.

AC2 — Edge case: Given an order is already marked Ready, when I attempt to change it back to Preparing, then the system prevents the change and keeps the status as Ready.


US-08: Mark Menu Items as Sold Out

Could-have

Staff
As a kitchen staff member, I want to mark menu items as sold out, so that customers do not order products that are unavailable.
AC1 — Normal: Given a menu item is available, when I mark it as Sold Out, then customers can see that the item is unavailable.

AC2 — Edge case: Given an item is already marked Sold Out, when a customer tries to add it to an order, then the system prevents the addition and displays an unavailable message.
