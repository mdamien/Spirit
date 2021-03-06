// Generated by CoffeeScript 1.7.1
(function() {
  describe("util format tests", function() {
    return it("formats a string", function() {
      var result;
      result = $.format("{foo} foobar {bar} {bad}", {
        foo: "foo text",
        bar: "bar text"
      });
      return expect(result).toEqual("foo text foobar bar text {bad}");
    });
  });

}).call(this);

//# sourceMappingURL=util-spec.map
