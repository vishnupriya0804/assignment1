
interface Payload{
    masskg:number;
  }
  
  class Astronaut implements Payload{
    masskg:number=0;
    name:string='';
  
    constructor(masskg:number,name:string){
      this.masskg=masskg
      this.name=name
    }
  }
  
  class Cargo implements Payload{
    masskg:number=0;
    material:string='';
    constructor(masskg:number,material:string){
      this.masskg=masskg
      this.material=material
    }
  }
  
  class Rocket{
    name:string='';
    totalcapacitykg:number=0;
    cargoitems:Cargo[]=[];
    astronaut:Astronaut[]=[];
    constructor(name:string,totalcapacitykg:number){
      this.name=name
      this.totalcapacitykg=totalcapacitykg
    }
    sumMass(items: Payload[]): number {
      let totalMass = 0;
  
      for (const item of items) {
        totalMass += item.masskg;
      }
  
      return totalMass;
    }
    currentMassKg(): number{
      return this.sumMass(this.cargoitems) + this.sumMass(this.astronaut) 
    }
    canAdd(item: Payload): boolean{
        if(this.currentMassKg() + item.masskg <=this.totalcapacitykg)
          return true;
        else
          return false;
       
    }
    addCargo(cargo: Cargo): boolean{
      let canno =this.canAdd(cargo) // decalring variable to receive the value
       if (canno){
        this.cargoitems.push(cargo);
        return true
      }
      
      else{
        return false
      }
       
    }
    addAstronaut(astronaut: Astronaut): boolean {
      if (this.canAdd(astronaut)) {
        this. astronaut.push(astronaut);
        return true;
      } else {
        return false;
      }
  }
  }
  const astronaut = new Astronaut(80, 'John');
  const cargo = new Cargo(5000, 'Satellite');
  const rocket = new Rocket('Falcon 9', 15000);
  
  
  
  // Add astronauts and cargo to the rocket
  rocket.addAstronaut(astronaut);
  
   rocket.addCargo(cargo);
  
   console.log(cargo);
