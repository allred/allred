FactoryGirl.define do
  factory :booking do
    start_at Faker::Date.forward(20) 
    end_at Faker::Date.forward(23) 
    client_email Faker::Internet.email 
    price "9.99"
    rental nil
  end
end
