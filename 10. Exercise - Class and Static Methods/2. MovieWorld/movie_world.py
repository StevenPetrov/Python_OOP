from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVDS = 15
    CUST = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVDS

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUST

    def id_check(self, name, id):
        for x in name:
            if x.id == id:
                return x

    def add_customer(self, customer: Customer):
        if len(self.customers) == self.CUST:
            return
        self.customers.append(customer)

    def add_dvd(self, dvds: DVD):
        if len(self.dvds) == dvds:
            return
        self.dvds.append(dvds)

    def rent_dvd(self, cust_it, dvd_it):
        customer = self.id_check(self.customers, cust_it)
        dvd = self.id_check(self.dvds, dvd_it)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, cust_it, dvd_it):
        customer = self.id_check(self.customers, cust_it)
        dvd = self.id_check(self.dvds, dvd_it)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers = ([repr(customer) for customer in self.customers])
        dvds = ([repr(dvd) for dvd in self.dvds])
        result = customers + dvds
        return '\n'.join(result)