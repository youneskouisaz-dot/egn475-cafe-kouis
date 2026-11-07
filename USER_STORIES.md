
# Café Calle Ocho — User Stories and Acceptance Criteria

**Course:** EGN475 — Prototyping  
**Project:** Café Calle Ocho  
**Personas:** Marta Alvarez (Customer) and Luis Rodriguez (Kitchen Staff)

## Priority Definitions

- **Must-have:** Essential for the working prototype.
- **Should-have:** Important but not essential for the first version.
- **Could-have:** Optional if time permits.

## US-01: View Café Menu

**Priority:** Must-have  
**Persona:** Marta Alvarez — Customer

**User Story:**  
As a café customer, I want to view the café menu, so that I can decide what to order.

**Acceptance Criteria:**

1. **Given** the café has menu items, **when** I open the menu page, **then** I see each item's name, price, and availability, including items marked Sold Out.
2. **Given** the café has no menu items, **when** I open the menu page, **then** I see a message saying the menu is currently empty.

## US-02: Add Items to an Order

**Priority:** Must-have  
**Persona:** Marta Alvarez — Customer

**User Story:**  
As a café customer, I want to add an available menu item to my order, so that I can select the food and drinks I want.

**Acceptance Criteria:**

1. **Given** an item is available and is not already in my order, **when** I click Add to Order, **then** the item appears in my order with a quantity of one.
2. **Given** an item is sold out, **when** I try to add it, **then** the item is not added and I see an unavailable message.

## US-03: View Order Summary

**Priority:** Must-have  
**Persona:** Marta Alvarez — Customer

**User Story:**  
As a café customer, I want to review my order summary, so that I can check my selected items and total before ordering.

**Acceptance Criteria:**

1. **Given** my order contains items, **when** I open the order summary, **then** I see each item's name, quantity, unit price, and a total calculated as the sum of quantity multiplied by unit price, excluding taxes and additional fees.
2. **Given** my order is empty, **when** I open the order summary, **then** I see an empty-order message and a total of $0.00.

## US-04: Submit an Order

**Priority:** Must-have  
**Persona:** Marta Alvarez — Customer

**User Story:**  
As a café customer, I want to submit my order, so that the café can receive it and I can get a confirmation number.

**Acceptance Criteria:**

1. **Given** my order contains at least one available item, **when** I click Place Order, **then** my order is saved and I receive a unique order number.
2. **Given** my order contains an item that became unavailable before submission, **when** I click Place Order, **then** the order is not submitted and I see a message identifying the unavailable item.

## US-05: Track Order Status

**Priority:** Must-have  
**Persona:** Marta Alvarez — Customer

**User Story:**  
As a café customer, I want to check my order's preparation status using its order number, so that I know when it is ready for pickup.

**Acceptance Criteria:**

1. **Given** I have a valid order number, **when** I enter it on the order tracking page and click Check Status, **then** I see the order's current status: Received, Preparing, or Ready.
2. **Given** the order number field is empty, incorrectly formatted, or does not match an existing order, **when** I click Check Status, **then** I see a clear error message and no order details are displayed.

## US-06: View Incoming Orders

**Priority:** Must-have  
**Persona:** Luis Rodriguez — Kitchen Staff

**User Story:**  
As a kitchen staff member, I want to view orders waiting for preparation, so that I know what food and drinks need to be prepared.

**Acceptance Criteria:**

1. **Given** customers have submitted orders with the status Received or Preparing, **when** I open the kitchen order board, **then** I see those orders with their order numbers, items, and statuses.
2. **Given** there are no orders with the status Received or Preparing, **when** I open the kitchen order board, **then** I see a message saying there are no pending orders.

## US-07A: Start Preparing an Order

**Priority:** Must-have  
**Persona:** Luis Rodriguez — Kitchen Staff

**User Story:**  
As a kitchen staff member, I want to mark a received order as Preparing, so that the kitchen and customer know preparation has started.

**Acceptance Criteria:**

1. **Given** an order has the status Received, **when** I click Start Preparing, **then** its status changes to Preparing.
2. **Given** an order is already Preparing or Ready, **when** I attempt to start preparing it again, **then** its existing status remains unchanged and I see a message explaining the action is not allowed.

## US-07B: Mark an Order Ready

**Priority:** Must-have  
**Persona:** Luis Rodriguez — Kitchen Staff

**User Story:**  
As a kitchen staff member, I want to mark a prepared order as Ready, so that the customer knows it can be picked up.

**Acceptance Criteria:**

1. **Given** an order has the status Preparing, **when** I click Mark Ready, **then** its status changes to Ready.
2. **Given** an order is still Received or is already Ready, **when** I attempt to mark it Ready, **then** its status remains unchanged and I see a message explaining that the change is not allowed.

## US-08: Mark Menu Items as Sold Out

**Priority:** Could-have  
**Persona:** Luis Rodriguez — Kitchen Staff

**User Story:**  
As a kitchen staff member, I want to mark an unavailable menu item as Sold Out, so that customers know they cannot order it.

**Acceptance Criteria:**

1. **Given** an item is currently available, **when** I mark it Sold Out on the staff menu page, **then** its availability changes to Sold Out and the customer menu displays that status.
2. **Given** an item is already marked Sold Out, **when** I attempt to mark it Sold Out again, **then** its status remains Sold Out and no duplicate change is made.

## Backlog Summary

| Story ID | Feature | Persona | Priority |
|---|---|---|---|
| US-01 | View Café Menu | Customer | Must-have |
| US-02 | Add Items to an Order | Customer | Must-have |
| US-03 | View Order Summary | Customer | Must-have |
| US-04 | Submit an Order | Customer | Must-have |
| US-05 | Track Order Status | Customer | Must-have |
| US-06 | View Incoming Orders | Staff | Must-have |
| US-07A | Start Preparing an Order | Staff | Must-have |
| US-07B | Mark an Order Ready | Staff | Must-have |
| US-08 | Mark Menu Items as Sold Out | Staff | Could-have |

**Total:** 9 stories, 18 acceptance criteria, 8 Must-have stories, and 1 Could-have story.
