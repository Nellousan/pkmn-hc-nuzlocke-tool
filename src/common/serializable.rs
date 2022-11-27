use crate::common::error::Error;
/// Every component should implement this, to add consistency on how saves are
/// loaded/saved throughout the entire program.
pub trait Serializable {
    /// Load component from data vector.
    fn load(&mut self, data: Vec<u8>);

    /// Outputs a Vec<u8> containing the data.
    fn save(&self) -> Result<Vec<u8>, Error>;
}
