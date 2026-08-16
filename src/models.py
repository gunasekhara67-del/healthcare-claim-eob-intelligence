from pydantic import BaseModel, Field


class ClaimAnalysis(BaseModel):
    claim_number: str = Field(description="Claim identification number")
    payer: str = Field(description="Insurance payer or health plan")
    status: str = Field(description="Claim status")
    denial_reason: str = Field(description="Reason for denial")
    billed_amount: float = Field(description="Amount billed")
    paid_amount: float = Field(description="Amount paid")
    patient_responsibility: float = Field(
        description="Amount the patient is responsible for"
    )
    recommended_action: str = Field(
        description="Recommended next action for the claim"
    )