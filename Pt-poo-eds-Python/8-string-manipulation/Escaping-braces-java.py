
# Using format with index for curly braces inside a java code
template = """
public class {0} {{
    public static void main(String[] args){{
        System.out.println("{1}");
    }}
}}
"""
print(template.format( "MyClass", "print('hello world')" ));


""" 
// Output --> valid java code
public class MyClass {
    public static void main(String[] args) {
        System.out.println("print('hello world')");
    }
} """