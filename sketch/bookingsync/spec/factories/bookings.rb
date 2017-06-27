FactoryGirl.define do
  factory :booking do
    start_at "2017-06-26 23:02:21"
    end_at "2017-06-26 23:02:21"
    #client_email "MyString"
    client_email Faker::Internet.email 
    price "9.99"
    rental nil
  end
end
