https://www.linkedin.com/jobs/view/software-development-engineer-i-at-expedia-group-4317703864/?skipRedirect=true&originalSubdomain=uk

# Expedia Java Prep

-  Encapsulation - is the process of combining data and functions that use that data into a single unit (class)
- Abstraction - is the process of hiding internal implementation details and showing only essential functionality to the user. (abstract class: contains abstract methods and they can have a body) (interface: contains abstract methods but they cant have a body)
- Inheritance: class inherits from another

- Composition: class has another class as a attribute.

- extend only when there is is-a relationship and behavior needs to be reused. Otherwise, use composition.


## Advanced techniques

- use 'var' when type is obvious from assignment. e.g. var map = new HashMap<String, List<Integer>>();

- dont use var when assignment is not obvious. e.g var result = result();

- use record for immutable data structures.

- use immutable collections when appropriete. List<String> names = List.of("A","B","C");

| Principle                 | Use                                                |
| ------------------------- | -------------------------------------------------- |
| **S**ingle responsibility | Class has one reason to change                     |
| **O**pen/closed           | Extendable without modifying existing code         |
| **L**iskov substitution   | Subclass should work everywhere parent is expected |
| **I**nterface segregation | Specific interfaces > single huge interface        |
| **D**ependency inversion  | Depend on abstractions                             |


- abstract methods must be implemented, concrete methods dont need to be overriden.

- String is immutable, use StringBuilder to modify strings efficiently.



- Use .equals for non primitive types as == would check if the object are the same

-  Do not hesitate to say that you don’t know the answer




# Learn 1 new Java a day

##