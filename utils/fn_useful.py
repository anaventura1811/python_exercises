from file_readers import read
import functools


def prop(prop_name: str):
  def getByProp(elem: str):
    return elem[prop_name]
  return getByProp


def nonEmpty(el: str) -> bool:
  return len(el) > 0

def nonInvalid(el: str) -> bool:
  try:
    int(el)
    return True
  except ValueError:
    return False

def get_unique_job_types(path: str) -> "list[str]":
  return list(set(filter(nonEmpty, map(prop("job_type"), read(path)))))
  

def get_unique_industries(path) -> "list[str]":
  return list(set(filter(nonEmpty, map(prop("industry"), read(path)))))

def get_max_salary(path: str) -> int:
  return max(
    map(
      int,
      filter(
        nonInvalid,
        filter(
          nonEmpty,
          map(
            prop("max_salary"),
            read(path)
          )
        )
      )
    )
  )


def get_min_salary(path: str) -> int:
  return min(
    map(
      int,
      filter(
        nonInvalid,
        filter(
          nonEmpty,
          map(
            prop("min_salary"),
            read(path)
          )
        )
      )
    )
  )


def filter_by_job_type(jobs: list, job_type: str) -> list:
  return list(filter(lambda job: job["job_type"] == job_type, jobs))


def filter_by_industry(jobs: list, industry: str) -> list:
  return list(filter(lambda job: job["industry"] == industry, jobs))


def curried_matches_salary_range(salary: int):
  def f(job: dict) -> bool:
    try:
      return matches_salary_range(job, salary)
    except ValueError:
      return False
  return f

def filter_by_salary_range(jobs: list, salary: int) -> list:
  return list(
    filter(
      curried_matches_salary_range(salary),
      jobs
    )
  )
