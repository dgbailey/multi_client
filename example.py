import foobarlib.foo as foo
import foobarlib.baz as baz
import foobarlib.bar as bar

name = "John Doe"
transformed_name = foo.fooify(name)
print(transformed_name)  # Output: "Foo John Doe"

numbers = [1, 2, 3, 4, 5]
#handled/unhandled exceptions in baz module sent to sentry_client_a DSN
average = baz.compute_average(numbers)
print(average)

#handled/unhandled exceptions in bar module sent to sentry_client_b DSN
# file_content = bar.read_file("data.txt")
# print(file_content)  # Output: Contents of the file

bar.write_file("output.txt", "Hello, World!")

