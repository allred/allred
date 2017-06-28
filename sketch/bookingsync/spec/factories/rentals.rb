FactoryGirl.define do
  factory :rental do
    name Faker::GameOfThrones.city
    daily_rate 1
  end
end
