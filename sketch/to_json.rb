#!/usr/bin/env ruby

class ToJson
  def initialize
  end

  def to_json(obj)
    if obj.is_a? Hash
      json = "{"
      json += obj.map {|k, v| %Q/"#{k}": /  + to_json(v)}.join(", ")
      json += "}"
      return json
    end
    if obj.is_a? Array
      json = "["
      json += obj.map {|e| to_json(e)}.join(", ")
      json += "]"
      return json
    end
    if obj.is_a? String
      return %Q/"#{obj}"/
    end
    if obj.is_a? Integer
      return obj.to_s
    end
    if obj.is_a? TrueClass
      return "true"
    end
    if obj.is_a? FalseClass
      return "false"
    end
  end
end

o = {
  k: "val",
  x: [1, 2],
}
t = ToJson.new
puts t.to_json(o)
