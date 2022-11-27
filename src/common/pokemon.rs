use crate::common::error::Error;
use crate::common::serializable::Serializable;

/// Pokemon trait
pub trait Pokemon: Serializable {
    fn get_species(&self) -> Result<u32, Error>;

    fn set_species(&mut self, species: u32) -> Result<(), Error>;

    fn get_level(&self) -> Result<u32, Error>;

    fn set_level(&mut self, level: u32) -> Result<(), Error>;

    fn get_happiness(&self) -> Result<u8, Error>;

    fn set_happiness(&mut self, happiness: u8) -> Result<(), Error>;

    fn get_ivs(&self) -> Result<&mut dyn IVs, Error>;

    fn get_evs(&self) -> Result<&mut dyn EVs, Error>;
}

pub trait IVs: Serializable {
    fn get_hp(&self) -> Result<u8, Error>;

    fn set_hp(&mut self, hp: u8) -> Result<(), u8>;

    fn get_atk(&self) -> Result<u8, Error>;

    fn set_atk(&mut self, atk: u8) -> Result<(), Error>;

    fn get_def(&self) -> Result<u8, Error>;

    fn set_def(&mut self, def: u8) -> Result<(), Error>;

    fn get_sp_atk(&self) -> Result<u8, Error>;

    fn set_sp_atk(&mut self, sp_atk: u8) -> Result<(), Error>;

    fn get_sp_def(&self) -> Result<u8, Error>;

    fn set_sp_def(&mut self, sp_def: u8) -> Result<u8, Error>;

    fn get_speed(&self) -> Result<(), Error>;

    fn set_speed(&mut self, speed: u8) -> Result<u8, Error>;
}

pub trait EVs: Serializable {
    fn get_hp(&self) -> Result<u8, Error>;

    fn set_hp(&mut self, hp: u8) -> Result<(), u8>;

    fn get_atk(&self) -> Result<u8, Error>;

    fn set_atk(&mut self, atk: u8) -> Result<(), Error>;

    fn get_def(&self) -> Result<u8, Error>;

    fn set_def(&mut self, def: u8) -> Result<(), Error>;

    fn get_sp_atk(&self) -> Result<u8, Error>;

    fn set_sp_atk(&mut self, sp_atk: u8) -> Result<(), Error>;

    fn get_sp_def(&self) -> Result<u8, Error>;

    fn set_sp_def(&mut self, sp_def: u8) -> Result<u8, Error>;

    fn get_speed(&self) -> Result<(), Error>;

    fn set_speed(&mut self, speed: u8) -> Result<u8, Error>;
}
