class Call < ApplicationRecord
  validates :number, presence: true, format: { with: /\A\+?[\d\s\-\(\)]+\z/, message: "must be a valid phone number" }
  
  enum status: {
    pending: 'pending',
    queued: 'queued',
    ringing: 'ringing',
    in_progress: 'in_progress',
    completed: 'completed',
    failed: 'failed',
    busy: 'busy',
    no_answer: 'no_answer',
    canceled: 'canceled'
  }
  
  scope :recent, -> { order(created_at: :desc) }
  scope :pending_or_queued, -> { where(status: ['pending', 'queued']) }
  
  def duration
    return nil unless started_at && finished_at
    (finished_at - started_at).to_i
  end
  
  def mark_as_started
    update(status: :ringing, started_at: Time.current)
  end
  
  def mark_as_completed
    update(status: :completed, finished_at: Time.current)
  end
  
  def mark_as_failed(reason = 'unknown')
    update(status: :failed, finished_at: Time.current)
  end
end

