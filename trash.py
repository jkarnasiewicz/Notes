# Django design patterns and best pratices

# app.py
Previously, there was no specific place for initializing the signal code. Typically, they
were imported or implemented in models.py (which was unreliable





# Gathering requirements:

1. Talk directly to the application owners even if they are not technical savvy.
2. Make sure you listen to their needs fully and note them.
3. Dont use technical jargon such as "models". Keep it simple and use end-user
   friendly terms such as a "user profile".
4. Set the right expectations. If something is not technically feasible or difficult,
   make sure you tell them right away.
5. Sketch as much as possible. Humans are visual in nature. Websites more so.
   Use rough lines and stick figures. No need to be perfect.
6. Break down process flows such as user signup. Any multistep functionality
   needs to be drawn as boxes connected by arrows.
7. Finally, work through the features list in the form of user stories or in any
   easy way to understand the form.
8. Play an active role in prioritizing the features into high, medium,
   or low buckets.
9. Be very, very conservative in accepting new features.
10. Post-meeting, share your notes with everyone to avoid misinterpretations.

+. Single-page document that quickly tells what the site is meant to be




# MODELS
# Structural patterns

# Patterns – normalized models
# denormalization(speed of the queries) and normalization(space with consistent data)
Problem: By design, model instances have duplicated data that cause data inconsistencies.
Solution: Break down your models into smaller models through normalization.
Connect these models with logical relationships between them.



# Pattern – model mixins
# Smaller mixins are better. Whenever a mixin becomes large and violates the Single
# Responsibility Principle, consider refactoring it into smaller classes. Let a mixin do
# one thing and do it well
Problem: Distinct models have the same fields and/or methods duplicated violating
the DRY principle.
Solution: Extract common fields and methods into various reusable model mixins.



# Pattern – service/utils objects
Problem: Models can get large and unmanageable. Testing and maintenance
get harder as a model does more than one thing.
Solution: Refactor out a set of related methods(e.g. @staticmethod or celery tasks)
into a specialized 'service' or 'utils' object.



# Retrieval patterns
# This section contains design patterns that deal with accessing model properties or
# performing queries on them.

# Pattern – property field
Problem: Models have attributes that are implemented as methods. However, these
attributes should not be persisted to the database.
Solution: Use the property decorator on such methods(@property)
# If it is an expensive calculation, we might want to cache the result(@cached_property)



# Pattern – custom model managers
Problem: Certain queries on models are defined and accessed repeatedly
throughout the code violating the DRY principle.
Solution: Define custom managers to give meaningful names to common queries



# VIEWS
# Pattern – context enhancers
Problem: Several views need the same context variable
Solution: Create a mixin or context processors(TEMPLATE_CONTEXT_PROCESSORS)
that sets the shared context variable



# Pattern – services
# This form of a service is usually called a web Application Programming Interface (API).
Problem: Information from your website is often scraped and processed by
other applications.
Solution: Create lightweight services that return data in machine-friendly formats,
such as JSON or XML(e.g. Django REST framework)



# TEMPLATES
# Pattern – template inheritance tree
Problem: Templates have lots of repeated content in several pages.
Solution: Use template inheritance wherever possible and include snippets elsewhere.

