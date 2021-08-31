export interface Campaign {
    id: string;
    name: string;
    description: string;
    representationLink: string;
    links: string[];
    create_date: Date;
  }

  export interface CampaignPage{
    next: string;
    previous: string;
    results: Campaign[];
  }