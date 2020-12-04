public class Ville {
    private String nomVille;
    private String nomPays;
    private int nbreHabitants;
    private char categorie;

    public Ville(){
	System.out.println("Création d'une ville !");
	nomVille = "Inconnu";
	nomPays = "Inconnu";
	nbreHabitants = 0;
	this.setCategorie();
    }

    public Ville(String pNom, int pNbre, String pPays)
	{
	    System.out.println("Création d'une ville avec des paramètres !");
	    nomVille = pNom;
	    nomPays = pPays;
	    nbreHabitants = pNbre;
	    this.setCategorie();
	}

    
	/** 
	 * @return String
	 */
	//Retourne le nom de la ville
    public String getNom()  {
	return nomVille;
    }

    
	/** 
	 * @return String
	 */
	//Retourne le nom du pays    
    public String getNomPays()
	{
	    return nomPays;
	}

    
	/** 
	 * @return int
	 */
	// Retourne le nombre d'habitants
    public int getNombreHabitants()
	{
	    return nbreHabitants;
	}

    
	/** 
	 * @return char
	 */
	//Retourne la catégorie de la ville
    public char getCategorie()
	{
	    return categorie;
	}

    
	/** 
	 * @param pNom
	 */
	//Définit le nom de la ville
    public void setNom(String pNom)
	{
	    nomVille = pNom;
	}

    
	/** 
	 * @param pPays
	 */
	//Définit le nom du pays
    public void setNomPays(String pPays)
	{
	    nomPays = pPays;
	}


    
	/** 
	 * @param nbre
	 * @throws NullPointerException
	 */
	//Définit le nombre d'habitants
    public void setNombreHabitants(int nbre)
	{
		if (nbre == 0)
			throw new NullPointerException("nbre can't be 0");
	    nbreHabitants = nbre;
	    this.setCategorie();
	}

    //Définit la catégorie de la ville
    private void setCategorie() {
	int bornesSuperieures[] = {0, 1000, 10000, 100000, 500000, 1000000, 5000000, 10000000};
	char categories[] = {'?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};

	int i = 0;
	while (i < bornesSuperieures.length && this.nbreHabitants > bornesSuperieures[i])
	    i++;
	this.categorie = categories[i];
    }

    
	/** 
	 * @return String
	 */
	//Retourne la description de la ville
    public String decrisToi(){
	return "\t"+this.nomVille+" est une ville de "+this.nomPays+ ", elle comporte : "+this.nbreHabitants+" habitant(s) => elle est donc de catégorie : "+this.categorie;
    }

    
	/** 
	 * @param v1
	 * @return String
	 */
	//Retourne une chaîne de caractères selon le résultat de la comparaison
    public String comparer(Ville v1){
	String str = new String();

	if (v1.getNombreHabitants() > this.nbreHabitants)
	    str = v1.getNom()+" est une ville plus peuplée que "+this.nomVille;
	else
	    str = this.nomVille+" est une ville plus peuplée que "+v1.getNom();
	return str;
    }

	
	/** 
	 * @param args
	 */
	public static void main(String[] args){
		System.out.println("Hello World");
	}
}
