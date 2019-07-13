#!/usr/bin/env ruby

def convert_temp(temp, **kwargs)
    input_scale = kwargs.fetch(:input_scale, "celsius")
    output_scale = kwargs.fetch(:output_scale, "celsius")
    if input_scale == output_scale
        return temp
    end
    case
        when input_scale == "fahrenheit"
          if output_scale == "celsius"
              return (temp - 32) * 5/9
          elsif output_scale == "kelvin"
              return (temp - 32) * 5/9 + 273.15
          end
        when input_scale == "celsius"
          if output_scale == "fahrenheit"
              return (temp * 9/5) + 32
          elsif output_scale == "kelvin"
              return temp + 273.15
          end
        when input_scale == "kelvin"
          if output_scale == "fahrenheit"
              return (temp - 273.15) * 9/5 + 32	
          elsif output_scale == "celsius"
              return temp - 273.15
          end
    end
end

puts convert_temp(0, input_scale: "celsius", output_scale: "fahrenheit")
