# Moneytor (💸 + 👀)

## What is the concept of Moneytor?

> Moneytor = 'Money' + 'to monitor'

Moneytor is an open source software designed to help people manage their finances. The user can put in all of his/her expenses and incomes and sort them based on different parameters.
Moneytor provides multiple ways to visualize the finances. The user can play with different filters to better analyze his/her finances.

The data is stored in a .csv spreadsheet, and is managed via the interface of our desktop application.

## What are the different features?

- First, let's set up the application:
  - Enter your **name**
  - Set a **password**
  - Choose your **preferred currency**

- Enter an **amount** of money and fill in:
  - The **name**
  - The **category** 
  - The **date** (if it's not the current date)
  - If it's an income or an expense
  - The **currency**

- Update or delete existing data

- You can create **projects** to organize your expenses (and then set up different settings)

- Data vizualisation (with filters)

> Our goal is to implement a maximum of our ideas.\
> Our first ideas for the design can be seen in the images folder.

If you want to find out more about our application and how to use it we recommend the [Wiki](https://github.com/charlottesarter/moneytor/wiki).

## What we did for the term project? 

We managed to implement **most of the features** that we wanted to have for our application, and a little bit more :)

#### What we did not manage to do

- Update or delete existing data: for now, you can only add a transaction
- One transaction file per user: it took really long to create a transaction file with sample data, so we did only one transaction file that we are using for all of the users
> If you log in as a different user, it will only change the preferred currency but not the displayed data. Due to time constraints, we have decided to leave it at that, as we are mainly focuesed on **demonstrating the features** of our program.

> Our only issue was a **lack of time** ⌛

#### What we did as a bonus

- We use live data to convert all of the transactions in the prefered currency of the logged user

> As it is taking a lot of time to convert all of the data, we, implemented this feature only for the plots, but not for the project list (we convert the data with fixed exchange rates).

## Ideas of improvement

- Provide more plots for data visualization and analysis
  - For example a line chart that displays all of the expenses by month for all of the years in one plot to compare them
- Provide more filters to display more precise and customized plots
- better verify the user's input (that is easy to do but just takes time)
- make the interface more appealing

## Authors 

- Max Eberlein
- Charlotte Sarter

As Team "🍋 Lemon Soju" :)
