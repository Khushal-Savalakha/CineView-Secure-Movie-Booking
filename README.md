# CineView Frontend

CineView is a secure and dynamic movie booking application that provides real-time updates, payment integration, and an intuitive user interface.  

## Features

- **User Authentication**: Secure login and signup system.  
- **Real-Time Booking Updates**: Ensures seat availability is always up-to-date.  
- **Payment Integration**: Seamless payments using **Stripe**.  
- **Movie Listings**: Displays all available movies with details.  
- **Booking History**: Users can view past and upcoming bookings.  
- **Responsive UI**: Built with **React & Tailwind CSS** for a smooth user experience.  

## Tech Stack

- **Frontend**: React, Redux, Tailwind CSS  
- **Backend**: Django REST Framework  
- **Database**: AWS RDS (MySQL)  

## Database Configuration

CineView uses **AWS RDS MySQL** as its primary database. Below is the configuration setup:  

### AWS RDS Security Groups

Here are the security group settings used to allow access to the **AWS RDS MySQL** database:  

![AWS RDS Security Group 1](https://github.com/user-attachments/assets/288efee3-6ed4-4b04-8487-af8990034fb6)  
![AWS RDS Security Group 2](https://github.com/user-attachments/assets/abd5eb47-9226-4e8d-84d1-c68a78e8d348)  
![AWS RDS Security Group 3](https://github.com/user-attachments/assets/00be4662-4bc6-42a2-bb19-fb5759c4a571)  
![AWS RDS Security Group 4](https://github.com/user-attachments/assets/21158201-2b03-430b-8b2a-b56b66faeddb)  

### Database Connection via DBeaver

The database is accessed and managed using **DBeaver**. Below are the connection details:  

![DBeaver Connection 1](https://github.com/user-attachments/assets/69749bca-8a21-4e42-b736-6ff9be8bd04b)  
![DBeaver Connection 2](https://github.com/user-attachments/assets/e6fadb2d-5be0-499c-9908-b85a7a906078)  
![DBeaver Connection 3](https://github.com/user-attachments/assets/b60096eb-04ef-4a9f-a7de-f6ac7c971fe9)  

---

## Getting Started

### Clone the Repository  

```bash
git clone https://github.com/Khushal-Savalakha/CineView-Frontend.git
cd CineView-Frontend
```

### Install Dependencies  

```bash
npm install
```

### Run the Application  

```bash
npm start
```

The frontend will be available at `http://localhost:3000`.  

---

## Backend Setup

Make sure the **Django backend** is running. Follow the backend repository for more details:  

[**CineView Backend**](https://github.com/Khushal-Savalakha/CineView-Backend)  
