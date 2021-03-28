package interfaces.twitter;


public class Tweet {
	
	private String text;
	private TwitterAccount twitterAccount;
	private Tweet orginalTweet;
	private int retweetCount = 0;
	
	public Tweet(TwitterAccount twitterAccount, String text) {
		this.text = text;
		this.twitterAccount = twitterAccount;
	}
	
	public Tweet(TwitterAccount twitterAccount, Tweet tweet) {
		if (twitterAccount == tweet.twitterAccount) {
			throw new IllegalArgumentException("Cant retweet yourself");
		}
		this.twitterAccount = twitterAccount;
		
		if (tweet.orginalTweet != null) {
			tweet.orginalTweet.retweetCount++;
			this.orginalTweet = tweet.orginalTweet;
			this.text = tweet.orginalTweet.text;
		} else {
			tweet.retweetCount++;
			this.orginalTweet = tweet;
			this.text = tweet.text;
		}
	}
	
	public String getText() {
		if (this.orginalTweet == null) {
			return text;			
		}
		return this.orginalTweet.getText();
	}
	
	public TwitterAccount getOwner() {
		return twitterAccount;
	}
	
	public Tweet getOriginalTweet() {
		return orginalTweet;
	}
	
	public int getRetweetCount() {
		return retweetCount;
	}
	
	@Override
	public String toString() {
		return this.getText();
	}
	
	public static void main(String[] args) {
		TwitterAccount ole = new TwitterAccount("Ole");
		TwitterAccount per = new TwitterAccount("Per");

		Tweet t1 = new Tweet(ole, "Twi");
		System.out.println(t1.getRetweetCount());
		Tweet t12 = new Tweet(per, t1);
		System.out.println(t1.getRetweetCount());
	}
}
	
