#!/usr/bin/env ruby
# purpose: like the unix "tail" command for Twitter
require 'term/ansicolor'
require 'bundler/setup'
require 'thor'
require 'twitter'

class Twail < Thor
  cs = 'F9y8Nbb3zCjvEnZv0cop8' + 'jm3rvi' + '5JP$\uajyGkLC.'
  cs = 'J' + cs
  cs = cs + 'k'
  cs.gsub!(/\$\\|\./, 'x')
  @@twitter = Twitter::REST::Client.new do |config|
    config.consumer_key = 'FJCpzTn5HvUthXtLmXTDEQ'
    config.consumer_secret = cs
  end
  @@color = Object.new.extend Term::ANSIColor
  @@colors_users = %w(
    cyan
    green
    magenta
    red
    yellow
  )

  desc "twail", "#{File.basename($0)} -u mikeallred -f .5 -c -l twail"
  method_option :color, :aliases => "-c", :desc => "enable ANSI color output", :lazy_default => true, :type => "boolean"
  method_option :follow, :aliases => "-f", :banner => ".5", :desc => "poll API every n minutes", :lazy_default => 1, :type => "numeric"
  method_option :list, :aliases => "-l", :banner => "twail", :desc => "print statuses for a list you own/follow", :lazy_default => "twail", :type => "string"
  method_option :user, :aliases => "-u", :banner => "mikeallred", :desc => "user name for logging into the API", :lazy_default => "mikeallred", :type => "string"
  def twail
    user = @@twitter.user(options[:user])
    list = nil
    tweets = []
    if options[:list]
      list = @@twitter.lists(user).select { |l| l.name == options[:list] }[0]
      unless list
        puts "list '#{options[:list]}' not followed or found in:"
        puts @@twitter.lists(user).map { |l| " #{l.name}" }
      end
    end
    if list
      tweets += @@twitter.list_timeline(list)
    end
    print_tweets(tweets)
    rescue Twitter::Error::TooManyRequests
      puts "rate limit error, reset in: ", error.rate_limit.reset_in
      sleep error.rate_limit.reset_in + 1
    #rescue Twitter::Error => e
    #  puts e.message, e
  end
  default_task :twail

  no_commands do
    def print_tweets(tweets)
      tweets.reverse_each do |t|
        puts sprintf("%s%15s%s %s|%s %s",
                     options[:color] && @@color.send(@@colors_users.sample),
                     t.user.screen_name,
                     options[:color] && @@color.reset,
                     options[:color] && @@color.blue,
                     options[:color] && @@color.reset,
                     t.text,
                    )
      end
    end
  end
end
Twail.start
