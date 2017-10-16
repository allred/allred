#!/usr/bin/env ruby
require 'byebug'
require 'em-http-request'

concurrency = 100
redirects = 1
urls = %w%
  http://google.com
  http://mikeallred.com
  http://facebook.com
  http://twitter.com
  http://yahoo.com
%

EM.run do
  EM::Iterator.new(urls, concurrency).each(
    proc {|url, iter|
      http = EventMachine::HttpRequest.new(url).get(:redirects => redirects)
      http.callback do |r|
        puts [url: url, status: r.response_header.status]
        iter.next
      end
      http.errback do
        puts [failed: url]
        iter.next
      end
    },
    proc {
      puts 'DONE'
      EM.stop
    }
  )
end

=begin
EventMachine.run do
  multi = EventMachine::MultiRequest.new
  multi.add :google, EventMachine::HttpRequest.new('http://google.com').get(:redirects => redirects_depth) 
  multi.add :mikeallred, EventMachine::HttpRequest.new('http://mikeallred.com').get(:redirects => redirects_depth)
  multi.callback do
    multi.responses[:callback]
    multi.responses[:errback]
    EventMachine.stop
  end
  #http1.callback {|a| puts a }
  #http1.errback { }
  #http2.callback {|a| puts a.response }
  #http2.errback { }
end
=end
