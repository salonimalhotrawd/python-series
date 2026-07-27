# @Program: Multiple Inheritance in Python
# @Author: Saloni Malhotra
# @Date: 27-07-2026

"""
=============================================================================
                     MULTIPLE INHERITANCE IN PYTHON
=============================================================================

-----------------------------------------------------------------------------
What is Multiple Inheritance?
-----------------------------------------------------------------------------

Multiple Inheritance is an Object-Oriented Programming (OOP) concept in
which a single child class inherits the properties (data members) and
methods (member functions) from two or more parent classes.

It allows a class to combine the functionality of multiple classes into
one class, making code more reusable and reducing duplication.

The child class can access all the accessible members of each parent class.

Syntax:

class Child(Parent1, Parent2, Parent3):
    pass

Python supports Multiple Inheritance.

-----------------------------------------------------------------------------


=============================================================================
                  METHOD RESOLUTION ORDER (MRO)
=============================================================================

-----------------------------------------------------------------------------
What is MRO?
-----------------------------------------------------------------------------

MRO stands for Method Resolution Order.

It is the order in which Python searches for methods and attributes when
they are called through an object.

Whenever a method or attribute is accessed, Python follows a predefined
sequence of classes to determine where that member exists.

If the required method is found, Python immediately stops searching.

MRO is especially important in Multiple Inheritance because multiple parent
classes may contain methods or attributes with the same name.

MRO removes this ambiguity by defining a fixed search order.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
Why is MRO Required?
-----------------------------------------------------------------------------

In Multiple Inheritance, two or more parent classes may have methods with
identical names.

Without MRO, Python would not know which method should be executed first.

MRO provides a clear and predictable path for searching methods and
attributes, ensuring that only one appropriate method is selected.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
How Does Python Decide the MRO?
-----------------------------------------------------------------------------

Python creates an ordered list of classes called the Method Resolution
Order (MRO).

While searching for a method or attribute, Python checks each class
according to this order until the required member is found.

Python internally uses the C3 Linearization Algorithm to generate the MRO.

This algorithm ensures:

• A class appears only once in the search order.
• The inheritance order defined by the programmer is respected.
• The search order remains consistent and predictable.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
MRO and super()
-----------------------------------------------------------------------------

The super() function always follows the Method Resolution Order (MRO).

It does NOT simply call the direct parent class.

Instead, it transfers control to the next class in the MRO.

This behavior allows all classes participating in Multiple Inheritance to
cooperate correctly without executing the same method multiple times.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
Advantages of Multiple Inheritance
-----------------------------------------------------------------------------

• Promotes code reusability.
• Allows combining features from multiple classes.
• Reduces duplicate code.
• Improves modularity by separating different responsibilities into
  different classes.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
Disadvantages of Multiple Inheritance
-----------------------------------------------------------------------------

• Increases code complexity.
• Can create ambiguity when multiple parent classes contain methods with
  the same name.
• Understanding MRO becomes essential.
• Poor design may reduce code readability and maintainability.

-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
Key Points
-----------------------------------------------------------------------------

✔ Multiple Inheritance allows a child class to inherit from multiple
  parent classes.

✔ MRO stands for Method Resolution Order.

✔ MRO defines the order in which Python searches for methods and
  attributes.

✔ Python follows the MRO whenever a method, attribute, or super() is used.

✔ Python uses the C3 Linearization Algorithm to calculate the MRO.

✔ object is always the final class in the Method Resolution Order.

=============================================================================

"""

# 1st @Program: Multiple Inheritance (Without super())
# _______________________________________________________


class Father:

    def __init__(self, father_name):
        print("Father Constructor Called")
        print("=" * 40)
        self.father_name = father_name

    def profession(self):
        print(f"{self.father_name} is an Engineer")

    def hobby(self):
        print("Father likes Cricket")


class Mother:

    def __init__(self, mother_name):
        print("Mother Constructor Called")
        print("=" * 40)
        self.mother_name = mother_name

    def profession(self):
        print(f"{self.mother_name} is a teacher")

    def hobby(self):
        print("Mother likes Singing")


# As per this order MRO decides which method is to call first
class Child(Father, Mother):

    def __init__(self, father_name, mother_name, child_name):
        print("Child Constructor Called")
        print("=" * 40)

        # Calling constructors manually
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

        self.child_name = child_name

    def introduction(self):
        print("\n----- Child Details -----")
        print("Child :", self.child_name)
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)

    def __str__(self):
        return f"The Father Name is {self.father_name}, Mother Name is {self.mother_name} and my name is {self.child_name}"


obj = Child("Sanjeev Malhotra", "Meena Malhotra", "Saloni Malhotra")

print(obj)
obj.profession()
obj.hobby()
obj.introduction()

print(Child.mro())

# 2nd @Program: Multiple Inheritance (Using super())
# ______________________________________________________________________________________


class FatherInheritance:

    def __init__(self, father_name, **kwargs):
        print("Father Constructor Called")

        self.father_name = father_name
        super().__init__(**kwargs)

    def profession(self):
        print(f"{self.father_name} is an Engineer")

    def hobby(self):
        print("Father likes Cricket")


class MotherInheritance:

    def __init__(self, mother_name, **kwargs):
        print("Mother Constructor Called")

        self.mother_name = mother_name
        super().__init__(**kwargs)

    def profession(self):
        print(f"{self.mother_name} is a Teacher")

    def hobby(self):
        print("Mother likes Singing")


class ChildInheritance(FatherInheritance, MotherInheritance):

    def __init__(self, father_name, mother_name, child_name):
        print("Child Constructor Called")

        self.child_name = child_name
        super().__init__(father_name=father_name, mother_name=mother_name)

    def introduction(self):
        print("\n----- Child Details -----")
        print("Child :", self.child_name)
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)


obj2 = ChildInheritance("Ashwani Dogra", "Anita Dogra", "Anmol Dogra")

obj2.profession()
obj2.hobby()
obj2.introduction()

print(ChildInheritance.mro())
