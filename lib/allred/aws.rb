require 'bundler/setup'
require 'aws-sdk'

module Allred
  class Aaws
    def route53
      Aws::Route53::Client.new(region: 'us-east-1')
    end
  end
end
