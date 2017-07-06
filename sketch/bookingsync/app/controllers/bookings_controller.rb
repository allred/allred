class BookingsController < ApplicationController
  before_action :set_rental
  before_action :set_rental_booking, only: [:show, :update, :destroy]

  def index
    json_response(@rental.bookings)
  end

  def show
    json_response(@booking)
  end

  def create
    @rental.bookings.create!(booking_params)
    json_response(@rental, :created)
  end

  def update
    @booking.update(booking_params)
    head :no_content
  end

  def destroy
    @booking.destroy
    head :no_content
  end

  private

  def booking_params
    params.permit(:start_at, :end_at, :client_email, :price)
    if params[:end_at] && params[:start_at]
      params[:price] = @rental.daily_rate * (params[:end_at].to_datetime - params[:start_at].to_datetime).to_i
    end
    #byebug
  end

  def set_rental
    @rental = Rental.find(params[:rental_id])
  end

  def set_rental_booking
    @booking = @rental.bookings.find_by!(id: params[:id]) if @rental
  end
end
