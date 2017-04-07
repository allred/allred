#!/usr/bin/env ruby
# need to point env var GOOGLE_APPLICATION_CREDENTIALS to json file path
require 'google/cloud/vision'
project_id = 'piloto-1473189293675'
vision = Google::Cloud::Vision.new project: project_id
file_name = ARGV[0]
labels = vision.image(file_name).labels

puts "Labels:"
labels.each do |l|
  puts l.description
end
