import 

class BoardContextMixin(ContextMixin):
"""
This mixin returns context with info related to user's campaign.
It can be used in any view that needs campaign-related info to a template.
"""
def get_campaigns(self):
    # Get the first campaign related to user, can be more in the future
    return self.request.user.campaign_set.all()

# Method Overwritten to pass campaign data to template context
def get_context_data(self, **kwargs):
    context = super(CampaignContextMixin).get_context_data(**kwargs)
    campaign = self.get_campaigns()[0]
    context['campaign_name'] = campaign.name
    context['campaign_start_date'] = campaign.start_date
    context['campaign_end_date'] = campaign.end_date
    context['org_name'] = self.request.user.organization.name
    context['campaign_image'] = campaign.image.url
    context['campaign_details'] = campaign.details
    return context
