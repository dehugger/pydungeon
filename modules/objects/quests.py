class Quest(object):

    def __init__(self):
        self.id
        self.name
        self.parent
        self.child
        self.complete
        self.reward_item
        self.reward_xp
        self.reward_effect #reward effect should be executable
        self.active
        self.objective

    def completeQuest(self):
        self.complete = True
        self.active = False
        return self.complete

    def getQuestRewardItem(self):
        return self.reward_item

    def getQuestRewardXP(self):
        return self.reward_xp

    def getQuestRewardEffect(self):
        return self.reward_effect
