package encapsulation;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;

public class Person {

	private String navn;
	private String epost;
	private String[] landskoder = {"ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "ye", "yt", "za", "zm", "zw"};
	private Date dato;
	private char gender;
	
	public String getName() {
		return navn;
	}
	
	public void setName(String navn) {
		String[] navnArr = navn.split(" ");
		if (navnArr.length != 2 || navnArr[0].length() < 3 || navnArr[1].length() < 3) {
			throw new IllegalArgumentException("Ikke gyldig navn");
		}
		this.navn = navn;
	}
	
	public void setEmail(String epost) {
		if (epost != null) {
			boolean valid = true;
			String[] epostArr = epost.split("\\.");
			if (epostArr.length != 3) {
				valid = false;
			} else if (!Arrays.stream(landskoder).anyMatch(epostArr[2]::equals)) {
				valid = false;
			} else if (epostArr[1].split("@").length != 2) {
				valid = false;
			}
			String[] navnArr = navn.split(" ");
			if (!epostArr[0].toLowerCase().equals(navnArr[0].toLowerCase()) || !epostArr[1].split("@")[0].toLowerCase().equals(navnArr[1].toLowerCase())) {
				valid = false;
			}
			if (!valid) {
				throw new IllegalArgumentException("Ikke gyldig epost");
			}
		}
		this.epost = epost;
	}
	
	public String getEmail() {
		return epost;
	}
	
	public void setBirthday(Date dato) {
		if (dato.getTime() > Calendar.getInstance().getTime().getTime()) {
			throw new IllegalArgumentException("Ikke gylig dato");
		}
		this.dato = dato;
	}
	
	public Date getBirthday() {
		return dato;
	}
	
	public void setGender(char gender) {
		if (gender == 'M' || gender == 'F' || gender == '\0') {
			this.gender = gender;
		} else {
			throw new IllegalArgumentException("Ikke gyldig kjønn");
		}
	}
	
	public char getGender() {
		return gender;
	}
	
	public static void main(String[] args) {
		Person p = new Person();
		p.setName("Mattis Hembre");
		p.setEmail("Mattis.Hembre@eventyr.no");
		p.setGender('M');
		System.out.println(p.getEmail());
				
	}
}
