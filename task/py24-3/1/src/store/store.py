import abc

class image_store(abc.ABC):
  @abc.abstractmethod
  def get_all(self) -> [list,Exception]:
    raise NotImplementedError
  @abc.abstractmethod
  def get_by_id(self, id:str) -> [str,Exception]:
    raise NotImplementedError
  @abc.abstractmethod
  def create(self) -> Exception:
    raise NotImplementedError
  # @abc.abstractmethod
  # def update(self) -> Exception:
  #   raise NotImplementedError
  @abc.abstractmethod
  def delete_all(self) -> Exception:
    raise NotImplementedError
  @abc.abstractmethod
  def delete_by_id(self, id:str) -> Exception:
    raise NotImplementedError