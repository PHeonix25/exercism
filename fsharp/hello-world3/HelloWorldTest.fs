module HelloWorldTest

open Xunit

open HelloWorld

[<Fact>]
let ``Say hi!`` () =
    Assert.Equal(hello, "Hello, World!")